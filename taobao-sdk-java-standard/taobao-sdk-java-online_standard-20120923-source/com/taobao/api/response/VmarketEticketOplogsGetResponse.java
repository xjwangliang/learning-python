package com.taobao.api.response;

import java.util.List;
import com.taobao.api.internal.mapping.ApiField;
import com.taobao.api.internal.mapping.ApiListField;
import com.taobao.api.domain.EticketOpLog;

import com.taobao.api.TaobaoResponse;

/**
 * TOP API: taobao.vmarket.eticket.oplogs.get response.
 * 
 * @author auto create
 * @since 1.0, null
 */
public class VmarketEticketOplogsGetResponse extends TaobaoResponse {

	private static final long serialVersionUID = 1232277626236957876L;

	/** 
	 * 操作日志列表
	 */
	@ApiListField("eticket_op_logs")
	@ApiField("eticket_op_log")
	private List<EticketOpLog> eticketOpLogs;

	/** 
	 * 符合条件的记录总数
	 */
	@ApiField("total_results")
	private Long totalResults;

	public void setEticketOpLogs(List<EticketOpLog> eticketOpLogs) {
		this.eticketOpLogs = eticketOpLogs;
	}
	public List<EticketOpLog> getEticketOpLogs( ) {
		return this.eticketOpLogs;
	}

	public void setTotalResults(Long totalResults) {
		this.totalResults = totalResults;
	}
	public Long getTotalResults( ) {
		return this.totalResults;
	}

}
