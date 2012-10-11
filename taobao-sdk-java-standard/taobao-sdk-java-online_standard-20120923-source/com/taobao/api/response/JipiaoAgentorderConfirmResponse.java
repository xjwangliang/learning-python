package com.taobao.api.response;

import com.taobao.api.internal.mapping.ApiField;

import com.taobao.api.TaobaoResponse;

/**
 * TOP API: taobao.jipiao.agentorder.confirm response.
 * 
 * @author auto create
 * @since 1.0, null
 */
public class JipiaoAgentorderConfirmResponse extends TaobaoResponse {

	private static final long serialVersionUID = 5157789459729161423L;

	/** 
	 * 确认出票是否成功
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
