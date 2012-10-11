package com.taobao.api.response;

import com.taobao.api.internal.mapping.ApiField;

import com.taobao.api.TaobaoResponse;

/**
 * TOP API: taobao.jipiao.agentorder.fail response.
 * 
 * @author auto create
 * @since 1.0, null
 */
public class JipiaoAgentorderFailResponse extends TaobaoResponse {

	private static final long serialVersionUID = 3161813433689388495L;

	/** 
	 * 失败订单是否成功
	 */
	@ApiField("is_success")
	private Boolean isSuccess;

	public void setIsSuccess(Boolean isSuccess) {
		this.isSuccess = isSuccess;
	}
	public Boolean getIsSuccess( ) {
		return this.isSuccess;
	}

}
